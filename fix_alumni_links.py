import re

with open('src/data.ts', 'r') as f:
    content = f.read()

links = [
    "https://www.linkedin.com/in/shristi-singh-a96b02267/",
    "https://www.linkedin.com/in/gaurav-jindal-354061141/",
    "https://www.linkedin.com/in/vihar-davuluri-40254326a/",
    "https://www.linkedin.com/in/ataullah-baig/",
    "https://www.linkedin.com/in/sk01234/",
    "https://www.linkedin.com/in/jagori-bandyopadhyay-b05760229/",
    "https://www.linkedin.com/in/veeransh/",
    "https://www.linkedin.com/in/sudeep-bhurat/",
    "https://www.linkedin.com/in/sushant-jha-87bb25226/",
    "https://www.linkedin.com/in/rishabh-mishra-0454a322b/",
    "https://www.linkedin.com/in/sahilj/",
    "https://www.linkedin.com/in/sourashis-chattopadhyay/",
    "https://www.linkedin.com/in/rushali-chakraborty-b68297a8/",
    "https://www.linkedin.com/in/samyak-jain-b09095208/",
    "https://www.linkedin.com/in/roshni-biswas23/",
    "https://www.linkedin.com/in/aditya-dubey-3329921b9/",
    "https://www.linkedin.com/in/apoorv-bansal-/",
    "https://www.linkedin.com/in/ragini-laskar-29b316192/",
    "https://www.linkedin.com/in/bhargaviadusumilli/",
    "https://www.linkedin.com/in/tanayaramane/",
    "https://www.linkedin.com/in/shachi-jalote/",
    "https://www.linkedin.com/in/abhishek-kabi/",
    "https://www.linkedin.com/in/nikitakishore/",
    "https://www.linkedin.com/in/aniketshah30/",
    "https://www.linkedin.com/in/-nikhil-kumar/",
    "https://www.linkedin.com/in/bhavik-jain-142545170/",
    None,
    "https://www.linkedin.com/in/amritashbharadwaj/",
    "https://www.linkedin.com/in/keshavgodala/",
    "https://www.linkedin.com/in/ishandas/",
    "https://www.linkedin.com/in/amrutha-sravya-mamidi-43b551190/",
    "https://www.linkedin.com/in/yasaswini-gedela/",
    None,
    None,
    "https://www.linkedin.com/in/tanishq-bansal-2104/",
    "https://www.linkedin.com/in/himanshudang/",
    "https://www.linkedin.com/in/gauranshi-chauhan/",
    "https://www.linkedin.com/in/debajit-chakraborty-iitkgp/",
    "https://www.linkedin.com/in/saswata-banerjee-iitkgp/"
]

alumni_start = content.find('alumni: [')
if alumni_start == -1:
    print("Could not find alumni section")
    exit(1)

alumni_end = content.find(']', alumni_start)
alumni_section = content[alumni_start:alumni_end]

lines = alumni_section.split('\n')
new_lines = []
link_idx = 0
for line in lines:
    if '{ name:' in line:
        # Check if already has a linkedin link, remove it first to be safe
        line = re.sub(r',\s*linkedin:\s*"[^"]*"', '', line)
        if link_idx < len(links) and links[link_idx]:
            # Add new linkedin link before closing brace
            line = line.replace(' }', f', linkedin: "{links[link_idx]}" }}')
        link_idx += 1
    new_lines.append(line)

new_alumni_section = '\n'.join(new_lines)
new_content = content[:alumni_start] + new_alumni_section + content[alumni_end:]

with open('src/data.ts', 'w') as f:
    f.write(new_content)

print("Done")
