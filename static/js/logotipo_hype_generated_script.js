//	HYPE.documents["logotipo"]

(function HYPE_DocumentLoader() {
	var resourcesFolderName = "logotipo_Resources";
	var documentName = "logotipo";
	var documentLoaderFilename = "logotipo_hype_generated_script.js";

	// find the URL for this script's absolute path and set as the resourceFolderName
	try {
		var scripts = document.getElementsByTagName('script');
		for(var i = 0; i < scripts.length; i++) {
			var scriptSrc = scripts[i].src;
			if(scriptSrc != null && scriptSrc.indexOf(documentLoaderFilename) != -1) {
				resourcesFolderName = scriptSrc.substr(0, scriptSrc.lastIndexOf("/"));
				break;
			}
		}
	} catch(err) {	}

	// load HYPE.js if it hasn't been loaded yet
	if(typeof HYPE == "undefined") {
		if(typeof window.HYPE_DocumentsToLoad == "undefined") {
			window.HYPE_DocumentsToLoad = new Array();
		}
		window.HYPE_DocumentsToLoad.push(HYPE_DocumentLoader);

		var headElement = document.getElementsByTagName('head')[0];
		var scriptElement = document.createElement('script');
		scriptElement.type= 'text/javascript';
		scriptElement.src = resourcesFolderName + '/' + 'HYPE.js';
		headElement.appendChild(scriptElement);
		return;
	}
	
	var attributeTransformerMapping = {"BoxShadowBlurRadius":"PixelValueTransformer","BackgroundColor":"ColorValueTransformer","BorderWidthBottom":"PixelValueTransformer","WordSpacing":"PixelValueTransformer","BoxShadowXOffset":"PixelValueTransformer","Opacity":"FractionalValueTransformer","BorderWidthRight":"PixelValueTransformer","BorderWidthTop":"PixelValueTransformer","BoxShadowColor":"ColorValueTransformer","BorderColorBottom":"ColorValueTransformer","FontSize":"PixelValueTransformer","BorderRadiusTopRight":"PixelValueTransformer","TextColor":"ColorValueTransformer","Rotate":"DegreeValueTransformer","Height":"PixelValueTransformer","BorderColorTop":"ColorValueTransformer","PaddingLeft":"PixelValueTransformer","Top":"PixelValueTransformer","BackgroundGradientStartColor":"ColorValueTransformer","TextShadowXOffset":"PixelValueTransformer","PaddingTop":"PixelValueTransformer","BackgroundGradientAngle":"DegreeValueTransformer","PaddingBottom":"PixelValueTransformer","PaddingRight":"PixelValueTransformer","BorderColorLeft":"ColorValueTransformer","Width":"PixelValueTransformer","TextShadowColor":"ColorValueTransformer","ReflectionOffset":"PixelValueTransformer","Left":"PixelValueTransformer","BorderRadiusBottomRight":"PixelValueTransformer","LineHeight":"PixelValueTransformer","ReflectionDepth":"FractionalValueTransformer","BorderColorRight":"ColorValueTransformer","BorderRadiusBottomLeft":"PixelValueTransformer","BorderWidthLeft":"PixelValueTransformer","TextShadowBlurRadius":"PixelValueTransformer","TextShadowYOffset":"PixelValueTransformer","BorderRadiusTopLeft":"PixelValueTransformer","BackgroundGradientEndColor":"ColorValueTransformer","BoxShadowYOffset":"PixelValueTransformer","LetterSpacing":"PixelValueTransformer"};

var scenes = [{"timelines":{"kTimelineDefaultIdentifier":{"framesPerSecond":30,"animations":[{"startValue":"20px","isRelative":true,"endValue":"17px","identifier":"Left","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8","startTime":0},{"startValue":"55px","isRelative":true,"endValue":"55px","identifier":"Top","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8","startTime":0},{"startValue":"0px","isRelative":true,"endValue":"390px","identifier":"Width","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8","startTime":0},{"startValue":"410px","isRelative":true,"endValue":"24px","identifier":"Left","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD","startTime":0},{"startValue":"89px","isRelative":true,"endValue":"89px","identifier":"Top","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD","startTime":0},{"startValue":"218px","isRelative":true,"endValue":"218px","identifier":"Height","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD","startTime":0},{"startValue":"0px","isRelative":true,"endValue":"388px","identifier":"Width","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD","startTime":0},{"startValue":"253px","isRelative":true,"endValue":"253px","identifier":"Height","duration":1.333333,"timingFunction":"easeinout","type":0,"oid":"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8","startTime":0},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.9333334,"timingFunction":"easeinout","type":0,"oid":"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8","startTime":0.4},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.9333334,"timingFunction":"easeinout","type":0,"oid":"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD","startTime":0.4},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F","startTime":0.8333333},{"startValue":"121px","isRelative":true,"endValue":"121px","identifier":"Left","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F","startTime":0.8333333},{"startValue":"147px","isRelative":true,"endValue":"147px","identifier":"Top","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F","startTime":0.8333333},{"startValue":"162px","isRelative":true,"endValue":"162px","identifier":"Height","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F","startTime":0.8333333},{"startValue":"219px","isRelative":true,"endValue":"219px","identifier":"Width","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F","startTime":0.8333333},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.3333334,"timingFunction":"easeinout","type":0,"oid":"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069","startTime":1.166667},{"startValue":"166px","isRelative":true,"endValue":"166px","identifier":"Left","duration":0.3333334,"timingFunction":"easeinout","type":0,"oid":"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069","startTime":1.166667},{"startValue":"205px","isRelative":true,"endValue":"205px","identifier":"Top","duration":0.3333334,"timingFunction":"easeinout","type":0,"oid":"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069","startTime":1.166667},{"startValue":"89px","isRelative":true,"endValue":"89px","identifier":"Height","duration":0.3333334,"timingFunction":"easeinout","type":0,"oid":"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069","startTime":1.166667},{"startValue":"70px","isRelative":true,"endValue":"70px","identifier":"Width","duration":0.3333334,"timingFunction":"easeinout","type":0,"oid":"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069","startTime":1.166667},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.3333333,"timingFunction":"easeinout","type":0,"oid":"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D","startTime":1.5},{"startValue":"227px","isRelative":true,"endValue":"227px","identifier":"Left","duration":0.3333333,"timingFunction":"easeinout","type":0,"oid":"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D","startTime":1.5},{"startValue":"220px","isRelative":true,"endValue":"220px","identifier":"Top","duration":0.3333333,"timingFunction":"easeinout","type":0,"oid":"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D","startTime":1.5},{"startValue":"70px","isRelative":true,"endValue":"70px","identifier":"Width","duration":0.3333333,"timingFunction":"easeinout","type":0,"oid":"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D","startTime":1.5},{"startValue":"88px","isRelative":true,"endValue":"88px","identifier":"Height","duration":0.3333333,"timingFunction":"easeinout","type":0,"oid":"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D","startTime":1.5},{"startValue":"265px","isRelative":true,"endValue":"342px","identifier":"Top","duration":0.7,"timingFunction":"easeinout","type":0,"oid":"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648","startTime":1.666667},{"startValue":"42px","isRelative":true,"endValue":"42px","identifier":"Height","duration":0.7,"timingFunction":"easeinout","type":0,"oid":"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648","startTime":1.666667},{"startValue":"363px","isRelative":true,"endValue":"363px","identifier":"Width","duration":0.7,"timingFunction":"easeinout","type":0,"oid":"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648","startTime":1.666667},{"startValue":"36px","isRelative":true,"endValue":"36px","identifier":"Left","duration":0.7,"timingFunction":"easeinout","type":0,"oid":"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648","startTime":1.666667},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.7,"timingFunction":"easeinout","type":0,"oid":"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648","startTime":1.666667}],"identifier":"kTimelineDefaultIdentifier","name":"Main Timeline","duration":2.366667}},"id":"1553E3C2-29CD-4160-B240-3331337D6D9F-7806-000012A47FFD7C17","sceneIndex":0,"perspective":"600px","oid":"1553E3C2-29CD-4160-B240-3331337D6D9F-7806-000012A47FFD7C17","initialValues":{"BA4415C7-2804-4856-B346-26959757D570-7806-000012C93C2966AD":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"410px","Display":"inline","BackgroundImage":"parte2.png","Height":"218px","Opacity":"0.000000","Overflow":"visible","ZIndex":"1","Top":"89px","Width":"0px","BackgroundSize":"100% 100%","TagName":"div"},"4CA7553A-74B0-4952-B410-0332620F25E1-7806-000012CE99F391F8":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"20px","Display":"inline","BackgroundImage":"parte1.png","Height":"253px","Opacity":"0.000000","Overflow":"visible","ZIndex":"2","Top":"55px","Width":"0px","BackgroundSize":"100% 100%","TagName":"div"},"D5B0BCF9-975B-40C9-AB7A-FA6FB32478DD-7806-000012D14CF1F20F":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"121px","Display":"inline","BackgroundImage":"casa.png","Height":"162px","Opacity":"0.000000","Overflow":"visible","ZIndex":"3","Top":"147px","Width":"219px","BackgroundSize":"100% 100%","TagName":"div"},"49D14A1E-31C7-4547-A139-F1856B97E573-7806-000012D7F2A62069":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"166px","Display":"inline","BackgroundImage":"R.png","Height":"89px","Opacity":"0.000000","Overflow":"visible","ZIndex":"5","Top":"205px","Width":"70px","BackgroundSize":"100% 100%","TagName":"div"},"CE880621-99B1-4144-96FF-A64E86395EAE-7806-000012D7F0DD3D4D":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"227px","Display":"inline","BackgroundImage":"H.png","Height":"88px","Opacity":"0.000000","Overflow":"visible","ZIndex":"4","Top":"220px","Width":"70px","BackgroundSize":"100% 100%","TagName":"div"},"ADED9A1D-FE73-4D94-A0E3-C4EABDEDCB3B-7806-000012D7F4BB5648":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"36px","Display":"inline","BackgroundImage":"titulo.png","Height":"42px","Opacity":"0.000000","Overflow":"visible","ZIndex":"6","Top":"265px","Width":"363px","BackgroundSize":"100% 100%","TagName":"div"}},"name":"Untitled Scene"}];

var javascriptMapping = {};


	
	var Custom = (function() {
	return {
	};
}());

	
	var hypeDoc = new HYPE();
	
	hypeDoc.attributeTransformerMapping = attributeTransformerMapping;
	hypeDoc.scenes = scenes;
	hypeDoc.javascriptMapping = javascriptMapping;
	hypeDoc.Custom = Custom;
	hypeDoc.currentSceneIndex = 0;
	hypeDoc.mainContentContainerID = "logotipo_hype_container";
	hypeDoc.resourcesFolderName = resourcesFolderName;
	hypeDoc.showHypeBuiltWatermark = 1;
	hypeDoc.showLoadingPage = false;
	hypeDoc.drawSceneBackgrounds = true;
	hypeDoc.documentName = documentName;

	HYPE.documents[documentName] = hypeDoc.API;

	hypeDoc.documentLoad(this.body);
}());

