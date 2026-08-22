const fs = require('fs');
// read image
let buf = fs.readFileSync('public/team/alumni/shristi-singh.jpg');
// convert to base64
let b64 = buf.toString('base64');
let tsContent = `export const shristiAvatar = "data:image/jpeg;base64,${b64}";\n`;
fs.writeFileSync('src/shristiAvatar.ts', tsContent);
console.log("Size:", tsContent.length);
