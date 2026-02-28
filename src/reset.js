const path = require('path');
const fs = require('fs-extra');
const chalk = require('chalk');
const readline = require('readline');

async function runReset(targetDir, options) {
  console.log('');
  console.log(chalk.bold('  arch-agent reset'));
  console.log('');

  const stateFile = path.join(targetDir, '.arch', 'state.json');

  if (!await fs.pathExists(stateFile)) {
    console.log(chalk.red('  No .arch/state.json found. Run `arch-agent init` first.\n'));
    process.exit(1);
  }

  const currentState = await fs.readJson(stateFile);
  const phase = currentState.current_phase || 'not_started';
  const decisions = currentState.decision_count || 0;

  if (phase === 'not_started' && decisions === 0) {
    console.log(chalk.dim('  State is already at initial state. Nothing to reset.\n'));
    return;
  }

  console.log(chalk.yellow(`  Current phase: ${phase}`));
  console.log(chalk.yellow(`  Decisions recorded: ${decisions}`));
  console.log(chalk.red('  This will reset state.json to initial state.'));
  console.log(chalk.red('  Phase outputs (.arch/phase*.md, .arch/components/*) will NOT be deleted.\n'));

  if (!options.yes) {
    const confirmed = await confirm('  Are you sure? (yes/no): ');
    if (!confirmed) {
      console.log(chalk.dim('\n  Cancelled.\n'));
      return;
    }
  }

  // Backup current state
  const backupPath = path.join(targetDir, '.arch', `state.backup.${Date.now()}.json`);
  await fs.copy(stateFile, backupPath);
  console.log(chalk.dim(`  Backed up to ${path.basename(backupPath)}`));

  // Write clean state (preserving project name)
  const templateState = await fs.readJson(
    path.join(__dirname, '..', 'templates', 'arch', 'state.json')
  );
  templateState.project_name = currentState.project_name || '';
  templateState.created_at = currentState.created_at || '';

  await fs.writeJson(stateFile, templateState, { spaces: 2 });
  console.log(chalk.green('  State reset to initial state.\n'));
}

function confirm(question) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer.toLowerCase() === 'yes');
    });
  });
}

module.exports = { runReset };
