npm init
npm install ol
npm install --save-dev parcel-bundler

Copy Code - https://openlayers.org/en/latest/doc/tutorials/bundle.html

Add follosing line in package.json:

"scripts": {
    ...
	"start": "parcel index.html",
    "build": "parcel build --public-url . index.html"
    ...
 }

 npm start