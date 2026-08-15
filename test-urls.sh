urls=(
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/McKinsey_%26_Company_1.svg/512px-McKinsey_%26_Company_1.svg.png"
  "https://upload.wikimedia.org/wikipedia/commons/3/34/Morgan_Stanley_Logo_1.svg"
  "https://upload.wikimedia.org/wikipedia/commons/f/fa/American_Express_logo_%282018%29.svg"
  "https://upload.wikimedia.org/wikipedia/commons/6/67/BlackRock_logo.svg"
  "https://upload.wikimedia.org/wikipedia/commons/a/af/J_P_Morgan_Logo_2008_1.svg"
  "https://upload.wikimedia.org/wikipedia/commons/6/61/Goldman_Sachs.svg"
  "https://upload.wikimedia.org/wikipedia/commons/a/a4/Deutsche_Bank_Logo_Ohne_Schrift.svg"
  "https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg"
  "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"
  "https://upload.wikimedia.org/wikipedia/commons/6/6f/Intuit_Logo.svg"
  "https://upload.wikimedia.org/wikipedia/commons/8/85/Procter_%26_Gamble_logo.svg"
  "https://upload.wikimedia.org/wikipedia/commons/f/ff/ITC_Limited_Logo.svg"
)

for url in "${urls[@]}"; do
  echo "Testing $url"
  curl -I -s "$url" | head -n 1
done
