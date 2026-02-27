const { execSync } = require('child_process');
const chalk = require('chalk');

function checkCommand(cmd) {
  try {
    const output = execSync(cmd, { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'] }).trim();
    return { ok: true, output };
  } catch {
    return { ok: false, output: null };
  }
}

async function runVerify(options = {}) {
  const quiet = options.quiet || false;

  if (!quiet) {
    console.log('');
    console.log(chalk.bold('  architor verify'));
    console.log('');
  }

  const results = [];

  const claude = checkCommand('claude --version');
  results.push({
    name: 'Claude Code',
    ok: claude.ok,
    version: claude.output,
    fix: 'Install Claude Code: https://docs.anthropic.com/en/docs/claude-code',
  });

  const python = checkCommand('python3 --version');
  results.push({
    name: 'Python 3',
    ok: python.ok,
    version: python.output,
    fix: 'Install Python 3: https://www.python.org/downloads/',
  });

  const git = checkCommand('git --version');
  results.push({
    name: 'git',
    ok: git.ok,
    version: git.output,
    fix: 'Install git: https://git-scm.com/downloads',
  });

  let allOk = true;
  for (const r of results) {
    if (r.ok) {
      if (!quiet) console.log(chalk.green(`  OK   ${r.name}: ${r.version}`));
    } else {
      allOk = false;
      console.log(chalk.red(`  FAIL ${r.name}: not found`));
      console.log(chalk.dim(`       ${r.fix}`));
    }
  }

  if (!quiet) {
    console.log('');
    if (allOk) {
      console.log(chalk.green('  All prerequisites met.\n'));
    } else {
      console.log(chalk.yellow('  Some prerequisites missing. Architor requires all of the above.\n'));
    }
  }

  return allOk;
}

module.exports = { runVerify };
