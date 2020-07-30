# Git One-person Workflow
Git is very useful when you are working on a project by yourself. How many times have you started editing a document, only to realize that you want to go back to a previous version? Git allows you to do just that.

![Git workflow](https://github.com/EnergyInsights/Intro-To-Python/blob/master/src/images/git-workflow.png "Logo Title Text 1")

## Initializing a local repo
1. Launch the command prompt (CMD).

2. Navigate to the lowest level of the project folder.
	- Open the folder in File Explorer
	- Copy the filepath to the clipboard (Ctrl-L, Ctrl-C)
	- In CMD, change directories using the following command:

		`cd C:\Users\me\Documents\SecretProject`

3. Initialize the Git repository.

		git init

4. Add files to the staging area.
	- To add all files in the project folder:

		`git add -A`

	- To add a specific file:

		`git add Recipes\SecretRecipe.txt`
5. Confirm all files which have been added to the staging area.

		git status
6. Commit your staging area to the repository.

		git commit -m "Customize this commit message"

## Adding a remote repo
Now that you have a local repo, let's add a remote repo.

1. Create a new repository on Github. [Github has posted instructions for doing this.](https://help.github.com/en/github/getting-started-with-github/create-a-repo)

2. In CMD, navigate to your local repository.

3. Add the remote repo as the **origin** for your local repo.
```
git remote add origin https://github.com/username/secretproject.git
```

4. Push your local *master* branch to the **origin**.
```
git push -u origin master
```

5. Verify your new remote repository on Github!

## Committing changes
As you work on Secret Project, you will reach natural checkpoints where you want to save your work. To save your work, commit your changes.

1. In CMD, navigate to your local repository.
2. (OPTIONAL) Verify the **diff**. If you are tracking files with a lot of formatting, this step may not be useful.
	```
	git diff
	```
3. Add files to the staging area.
	```
	git add  Recipes\RecipeScraping.py
	```
4. Confirm all files which have been added to the staging area.
	```
	git status
	```
5. Commit your staging area to the local repository.
	```
	git commit -m "Customize this commit message"
	```
6. Push your local changes to the remote repository.
	```
	git push origin master
	```