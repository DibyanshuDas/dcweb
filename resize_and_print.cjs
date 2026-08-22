const fs = require('fs');
const sharp = require('sharp');

const files = [
  'shristi-singh.jpg',
  'gaurav-jindal.jpg',
  'vihar-davuluri.jpg',
  'ataullah-baig.jpg',
  'sagar-kumar.jpg',
  'jagori-bandyopadhyay.jpg',
  'veeransh-mehta.jpg',
  'sudeep-bhurat.jpg',
  'sushant-jha.jpg'
];

async function run() {
  let output = 'export const alumniAvatars = {\n';
  for (const file of files) {
    const path = `public/team/alumni/${file}`;
    if (!fs.existsSync(path)) continue;
    const buffer = await sharp(path)
      .resize(250, 250, { fit: 'cover' })
      .jpeg({ quality: 75 })
      .toBuffer();
    const b64 = buffer.toString('base64');
    output += `  "${file}": "data:image/jpeg;base64,${b64}",\n`;
  }
  output += '};\n';
  fs.writeFileSync('src/alumniAvatars.ts', output);
  console.log('Done! Size of generated file:', output.length);
}

run();
