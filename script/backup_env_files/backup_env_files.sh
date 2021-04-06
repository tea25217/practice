files=( \
"$HOME/.profile" \
"$HOME/.bashrc" \
"$HOME/.bash_profile" \
"$HOME/.bash_aliases" \
"$HOME/.sommelierrc" \
"/etc/systemd/user/cros-garcon.service.d/cros-garcon-override.conf" \
)

if ! [ -d backup ]; then
  mkdir backup
fi

for file in ${files[@]};
do
  if [ -f $file ]; then
    cp -f $file backup/
  fi
done
