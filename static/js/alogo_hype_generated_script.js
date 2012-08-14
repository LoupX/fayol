//	HYPE.documents["alogo"]

(function HYPE_DocumentLoader() {
	var resourcesFolderName = "alogo_Resources";
	var documentName = "alogo";
	var documentLoaderFilename = "alogo_hype_generated_script.js";

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

var scenes = [{"timelines":{"kTimelineDefaultIdentifier":{"framesPerSecond":30,"animations":[{"startValue":"-180deg","isRelative":true,"endValue":"0deg","identifier":"Rotate","duration":1.666667,"timingFunction":"easeinout","type":0,"oid":"A4370992-3432-4590-9507-C23CDAE813AD-23210-00016DCA21D2D403","startTime":0},{"startValue":"180deg","isRelative":true,"endValue":"0deg","identifier":"Rotate","duration":1.666667,"timingFunction":"easeinout","type":0,"oid":"B2914215-62B9-4F5D-A4CD-C0B0176CB897-23210-00016DCC6BD8C934","startTime":0},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":1.166667,"timingFunction":"easeinout","type":0,"oid":"A4370992-3432-4590-9507-C23CDAE813AD-23210-00016DCA21D2D403","startTime":0.5},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"B2914215-62B9-4F5D-A4CD-C0B0176CB897-23210-00016DCC6BD8C934","startTime":1},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.8333333,"timingFunction":"easeinout","type":0,"oid":"22EF3C75-8DF7-42C9-8135-351E0DE8016D-23210-00016DCEC580405E","startTime":1.466667},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"AD14619C-2308-4EF3-A861-CFCCA0945D4A-23210-00016DD6BB6BDE1A","startTime":2},{"startValue":"297.762px","isRelative":true,"endValue":"327px","identifier":"Top","duration":1,"timingFunction":"easeinout","type":0,"oid":"5490A0EB-BB97-4BB7-BC42-2A7A380067EF-23210-00016DDE688B946A","startTime":2},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.6666667,"timingFunction":"easeinout","type":0,"oid":"1F940B68-9A45-4F33-BAE9-1C48B4ACF179-23210-00016DD91C68359B","startTime":2.333333},{"startValue":"0.000000","isRelative":true,"endValue":"1.000000","identifier":"Opacity","duration":0.6333332,"timingFunction":"easeinout","type":0,"oid":"5490A0EB-BB97-4BB7-BC42-2A7A380067EF-23210-00016DDE688B946A","startTime":2.366667}],"identifier":"kTimelineDefaultIdentifier","name":"Main Timeline","duration":3}},"id":"68B029EF-EABC-4728-A8A4-C21F10ECC5A4-23210-00016DAAD08A64DF","sceneIndex":0,"perspective":"600px","oid":"68B029EF-EABC-4728-A8A4-C21F10ECC5A4-23210-00016DAAD08A64DF","initialValues":{"5490A0EB-BB97-4BB7-BC42-2A7A380067EF-23210-00016DDE688B946A":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"18.1055px","Display":"inline","BackgroundImage":"titulo.png","Height":"42px","Opacity":"0.000000","Overflow":"visible","ZIndex":"6","Top":"297.762px","Width":"363px","BackgroundSize":"100% 100%","TagName":"div"},"AD14619C-2308-4EF3-A861-CFCCA0945D4A-23210-00016DD6BB6BDE1A":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"155px","Display":"inline","BackgroundImage":"R.png","Height":"89px","Opacity":"0.000000","Overflow":"visible","ZIndex":"4","Top":"204px","Width":"70px","BackgroundSize":"100% 100%","TagName":"div"},"A4370992-3432-4590-9507-C23CDAE813AD-23210-00016DCA21D2D403":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"8px","Display":"inline","BackgroundImage":"parte2.png","Height":"218px","Opacity":"0.000000","Overflow":"visible","Top":"85px","Width":"388px","ZIndex":"1","BackgroundSize":"100% 100%","TagName":"div","Rotate":"-180deg"},"B2914215-62B9-4F5D-A4CD-C0B0176CB897-23210-00016DCC6BD8C934":{"BackgroundColor":"","Position":"absolute","BackgroundOrigin":"content-box","Left":"5px","Display":"inline","BackgroundImage":"parte1-1-1.png","ReflectionOffset":"8px","Height":"253px","Opacity":"0.000000","Width":"390px","Overflow":"visible","Top":"51px","BackgroundRepeat":"no-repeat","ReflectionDepth":"0.000000","TagName":"div","ZIndex":"2","BackgroundSize":"100% 100%","Rotate":"180deg"},"1F940B68-9A45-4F33-BAE9-1C48B4ACF179-23210-00016DD91C68359B":{"Position":"absolute","BackgroundOrigin":"content-box","Left":"216px","Display":"inline","BackgroundImage":"H.png","Height":"88px","Opacity":"0.000000","Overflow":"visible","ZIndex":"5","Top":"216px","Width":"70px","BackgroundSize":"100% 100%","TagName":"div"},"22EF3C75-8DF7-42C9-8135-351E0DE8016D-23210-00016DCEC580405E":{"ActionOnMouseUp":{"type":0},"BorderWidthBottom":"0px","Opacity":"0.000000","Display":"inline","BorderStyleRight":"None","BorderStyleBottom":"None","Top":"143px","BackgroundImage":"casa.png","BorderWidthRight":"0px","BorderStyleLeft":"None","Position":"absolute","Height":"162px","Left":"110px","BorderStyleTop":"None","Width":"219px","ZIndex":"3","BackgroundOrigin":"content-box","BorderWidthTop":"0px","BackgroundSize":"100% 100%","Overflow":"visible","BorderWidthLeft":"0px","TagName":"div"}},"name":"Untitled Scene"}];

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
	hypeDoc.mainContentContainerID = "alogo_hype_container";
	hypeDoc.resourcesFolderName = resourcesFolderName;
	hypeDoc.showHypeBuiltWatermark = 1;
	hypeDoc.showLoadingPage = false;
	hypeDoc.drawSceneBackgrounds = true;
	hypeDoc.documentName = documentName;

	HYPE.documents[documentName] = hypeDoc.API;

	hypeDoc.documentLoad(this.body);
}());

