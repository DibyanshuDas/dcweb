const Jimp = require('jimp');
Jimp.read('public/team/alumni/shristi-singh.jpg')
  .then(image => {
    return image
      .resize(300, Jimp.AUTO) 
      .quality(80) 
      .getBase64Async(Jimp.MIME_JPEG);
  })
  .then(b64 => {
    const tsContent = `export const shristiAvatar = "${b64}";\n`;
    require('fs').writeFileSync('src/shristiAvatar.ts', tsContent);
    console.log("Size:", tsContent.length);
  })
  .catch(err => {
    console.error(err);
  });
