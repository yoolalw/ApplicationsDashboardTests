const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const root = path.resolve(__dirname, '..');

function run(cmd, args) {
  console.log(`\n> ${cmd} ${args.join(' ')}`);
  const res = spawnSync(cmd, args, { cwd: root, stdio: 'inherit', shell: true });
  if (res.status !== 0) {
    console.error(`Erro ao executar o comando: ${cmd} ${args.join(' ')}`);
    process.exit(res.status || 1);
  }
}

console.log('=== Iniciando empacotamento do Applications Dashboard (Windows e Linux) ===\n');

// 1. Executar o build do Vite + Esbuild (server.cjs)
run('npm', ['run', 'build']);

// 2. Empacotamento para Windows
if (process.platform === 'win32') {
  console.log('\n--- Criando release Windows Portatil e ZIP ---');
  run('node', ['scripts/package-portable.cjs']);
  run('powershell', [
    '-NoProfile',
    '-Command',
    '"Compress-Archive -Path release/APPDashboard/* -DestinationPath release/APPDashboard-windows-portable.zip -Force"'
  ]);
} else {
  console.log('\n--- Criando release Windows via electron-builder ---');
  run('npx', ['electron-builder', '--win', '--publish', 'never']);
}

// 3. Empacotamento para Linux
console.log('\n--- Criando release Linux (.tar.gz) ---');
run('npx', ['electron-builder', '--linux', '--publish', 'never']);

console.log('\n=== Processo de empacotamento concluido com sucesso! ===');
console.log('Releases geradas em release/ (Windows) e dist/ (Linux).');
