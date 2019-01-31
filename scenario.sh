PS1='(demo_machine) ${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)'
whoami
ls
pwd
#expect: glory
ls
echo $PS1
echo $PROMPT