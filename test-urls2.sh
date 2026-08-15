urls=(
  "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Boston_Scientific_logo.svg/1024px-Boston_Scientific_logo.svg.png"
  "https://alpha-grep.com/wp-content/uploads/2022/01/logo-color.png"
  "https://quadeye.com/wp-content/uploads/2021/10/logo.png"
)

for url in "${urls[@]}"; do
  echo "Testing $url"
  curl -I -s "$url" | head -n 1
done
