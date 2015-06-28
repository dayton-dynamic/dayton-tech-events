docker run -d -v "$PWD:/src" -p 4000:4000 grahamc/jekyll serve -H 0.0.0.0
echo "Site available at http://localhost:4000/"
