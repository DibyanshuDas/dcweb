import fs from 'fs';
import https from 'https';
import path from 'path';

const links = {
  "shristi-singh.jpg": "https://media.licdn.com/dms/image/v2/D4D03AQFWDR7KJ3DvJA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1688387753881?e=1788998400&v=beta&t=Q_YcUHahhS42qqQcnw7NzJZHB6mj-wYh2N2S225U_t8",
  "gaurav-jindal.jpg": "https://media.licdn.com/dms/image/v2/D5603AQHLdZiMTRvvnw/profile-displayphoto-crop_800_800/B56ZgSvceHHkAI-/0/1752661085119?e=1788998400&v=beta&t=BVrS3cmqcbebvFw-_dAreGxYRbeORnxgZkaX9fyvmro",
  "vihar-davuluri.jpg": "https://media.licdn.com/dms/image/v2/D5603AQFS3Kiez50Hhw/profile-displayphoto-shrink_800_800/B56ZOYdh7XGwAk-/0/1733429715948?e=1788998400&v=beta&t=-ryroLz7G5iC88VORa37y9AhvgXtseq12UiAhqRPBt4",
  "ataullah-baig.jpg": "https://media.licdn.com/dms/image/v2/D5603AQEsL3jEy63Fnw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718308516052?e=1788998400&v=beta&t=bPSoEmCumBB3_DOK5jr6UFq8LmVPcOaNAIAKK8bnVTY",
  "sagar-kumar.jpg": "https://media.licdn.com/dms/image/v2/D5603AQH2ILjgeEsG-g/profile-displayphoto-crop_800_800/B56Z.BjP8OHIAI-/0/1784584930463?e=1788998400&v=beta&t=ZEYbgKN25HfzB_geb7VwM8NMn9PU_CRfDNSC7FbNPoY",
  "jagori-bandyopadhyay.jpg": "https://media.licdn.com/dms/image/v2/D4D03AQElbdM0KtoUQA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1681640170360?e=1788998400&v=beta&t=qBHGd7JPiEY8skdLSz9A5XoCXLxecJzdd0eyoTRyd_U",
  "veeransh-mehta.jpg": "https://media.licdn.com/dms/image/v2/D4D03AQFaPFBkTPcxrA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1678776403437?e=1788998400&v=beta&t=R0Kr_QMHfFKovAlqQ7gl745hzObaIhQL8eksUXGIbDo",
  "sudeep-bhurat.jpg": "https://media.licdn.com/dms/image/v2/D5603AQHquuSFPlXrwg/profile-displayphoto-shrink_800_800/B56ZZO5BSWGoAc-/0/1745080299190?e=1788998400&v=beta&t=tX6FkZGFwPlf7HukNdrL2sNS9ccPqQuw_S20xKXgn4Y",
  "sushant-jha.jpg": "https://media.licdn.com/dms/image/v2/D5603AQHv1WQTydz48Q/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1684697354367?e=1788998400&v=beta&t=GlgoQgPQn4h7DxQO2SsvAMrH_QhrtfzyeQpAMFbaISs"
};

const dir = path.join(process.cwd(), 'public', 'team', 'alumni');
if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir, { recursive: true });
}

async function downloadImages() {
  const promises = Object.entries(links).map(([filename, url]) => {
    return new Promise((resolve, reject) => {
      const dest = path.join(dir, filename);
      const file = fs.createWriteStream(dest);
      
      https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (response) => {
        response.pipe(file);
        file.on('finish', () => {
          file.close(resolve);
        });
      }).on('error', (err) => {
        fs.unlink(dest, () => reject(err));
      });
    });
  });

  try {
    await Promise.all(promises);
    console.log('All alumni avatars downloaded successfully.');
  } catch (err) {
    console.error('Error downloading avatars:', err);
  }
}

downloadImages();
