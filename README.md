# svdiff-pytorch

Download the files or clone the git repository and change the directory to the present directory on the terminal.
Run docker build -t svdiff-pytorch in the terminal
Run docker run -p 8000:8000 svdiff-pytorch
Run curl -X POST -H "Content-Type: application/json" -d '{
  "prompt": "<Your message>"
}' http://localhost:8000/prompt-req
.
