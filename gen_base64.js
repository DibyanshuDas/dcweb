import fs from 'fs';
let buf = fs.readFileSync('public/team/alumni/shristi-singh.jpg');
let b64 = buf.toString('base64');
let tsContent = `export const shristiAvatar = "data:image/jpeg;base64,${b64}";\n`;
fs.writeFileSync('src/shristiAvatar.ts', tsContent);
