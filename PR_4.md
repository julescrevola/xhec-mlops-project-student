Before working on this branch, include your previous work from steps 1, 2 and 3 (which have been merged to the main branch) in your branch:

```bash
git checkout main
git pull
git checkout 4/deploy_model_api
git rebase main
```

The goal of this PR is to:

- [ ] Create a FastAPI API to make predictions on new data
- [ ] Dockerize the API

Files to be modified: 
- [ ] the `src/web_service` folder
- [ ] Dockerfile.app
- [ ] Add any other file you find relevant to help you with the deployment work

Recommendation: you should first make the Fast API work locally before trying to run it on a docker container.

Notes:

- [ ] Don't forget to update the README.md with the steps to reproduce to run the API (inside the docker container)
- [ ] Finalize the README.md so you include all the instructions presented initially
- [ ] (Make sure the REAMDE.md is not the initial one from the template)
- [ ] Help - For the `docker run` command, bind the ports as follows: `-p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201`

___

*TODO: delete this markdown file before merging the pull request*