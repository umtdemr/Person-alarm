push_git:
	echo "Pushing to git $(c)"
	git add .
	git commit -m "$(c)"
	git push
