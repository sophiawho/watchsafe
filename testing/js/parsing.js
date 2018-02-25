// Parsing JSON so we can Plotly our response
// initialize our arrays
var x = [],
nudey = [],
weapony = [],
alcoholy = [], 
drugsy = [];

data = JSON.parse(msg);

// intialize x which is time samples, one per second 
for (var i = 0; i<data.length; i++){
	x.push(i);
}

msg.data.frames.forEach(function (entry) index){
	nudey.push(frames.nudity);
	weapony.push(frames.weapon);
	drugsy.push(frames.drugs);
	alcoholy.push(frames.alcohol);
}