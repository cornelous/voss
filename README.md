# My First Python and Flask App

A currency converter as a fulfilment for a tech assessment.

## Installation Process - nix based

1. Open a terminal and run

```bash
    git clone https://github.com/cornelous/voss.git
 ```

 ```bash
    cd voss
```

```bash
    docker build -t currency-converter-image .
```

```bash
    docker run -d --name currency-converter-container -p 80:80 currency-converter-image
```

2. Then Visit app at http://127.0.0.1/ in your browser

## NB
This is my very first python and flask, I enjoyed the experience of
putting it together. I still have lots to learn!

I may have commmited some files that maybe needed to be in .gitignore

My unit tests are incomplete, I was going to test for these 3 scenarios
- test that non-supported currencies can not be submitted
- test that given a base and a target, a number is returned 
- test that EUR to EUR conversion fails as this is NOT supported by API
