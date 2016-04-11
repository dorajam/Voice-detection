let multiplied = false;
let drawVisual = null;

const HEIGHT = window.innerHeight;
const WIDTH = window.innerWidth;

let canvas = document.getElementById("canvas")
let canvasCtx = canvas.getContext("2d");

canvas.height = HEIGHT;
canvas.width = WIDTH;
// navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;

navigator.mediaDevices.getUserMedia( {audio: true})
    .then((stream) => {
        let audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        var source = audioCtx.createMediaStreamSource(stream);

        let analyser = audioCtx.createAnalyser();
        source.connect(analyser);

        analyser.fftSize = 2048;

        let bufferLength = analyser.frequencyBinCount;
        let dataArray = new Uint8Array(bufferLength);

        // console.log(fftBinWidth);  // 21
        const fftBinWidth = audioCtx.sampleRate / analyser.fftSize;
        const numBins = 40;
        const numPoints = numBins + 2;
        const numSections = numPoints - 1;
        const melDataArray = new Float32Array(numBins);

        const buffer = [];
        const melWidth = hzToMel(8000) / numSections;


        function fromFFTtriangle(input) {
            for (let i=0; i < melDataArray.length; i++){
                let multipliers = [];
                let minHz = melToHz(i * melWidth);
                let centerHz = melToHz((i + 1) * melWidth);
                let maxHz = melToHz((i + 2) * melWidth);

                let slopeAscending = 1/(centerHz - minHz);
                let slopeDescending = 1/(centerHz - maxHz);    // this needs to be negative!!!!

                let minInputIndex = (minHz / fftBinWidth);
                let maxInputIndex = (maxHz / fftBinWidth);
                
                melDataArray[i] = 0.0;

                for (let j = minInputIndex; j < maxInputIndex; j++) {
                    let mult;
                    let hzVal = j * fftBinWidth;
                    if (hzVal < centerHz) {
                        mult = (hzVal - minHz) * slopeAscending;
                    } else {
                        mult = 1 + (hzVal - centerHz) * slopeDescending;
                    }
                    if (mult < 0) {
                        multipliers.push(mult);
                    }
                    melDataArray[i] += mult * input[Math.floor(j)];
                }
                melDataArray[i] = Math.log(melDataArray[i] + 1);
                // if (!multiplied)  console.log(multipliers);
            }
            // multiplied = true;
        }
        
        
        const draw = () => {
            drawVisual = requestAnimationFrame(draw);
            analyser.getByteFrequencyData(dataArray);

            fromFFTtriangle(dataArray);

            let DCTarray = DCT(melDataArray);

            if (buffer.length > 40) {
                buffer.shift();
            }
            buffer.push(DCTarray);

            canvasCtx.fillStyle = "rgba(255,255,255, 0.15)";
            canvasCtx.fillRect(0, 0, WIDTH, HEIGHT);

            let barWidth = (WIDTH/ DCTarray.length);
            // let r =  255;
            // let g = Math.sin(new Date() / 5000);
            // let b = Math.sin(new Date() / 4000);
            // if(g < 0 || b < 0) {
            //     g = Math.abs(g);
            //     b = Math.abs(b);
            // }
            // if(g < 0.5 || b < 0.5) {
            //     g = g + 0.3;
            //     b = b + 0.3;
            // }
            // if(g > 0.8 || b > 0.8) {
            //     g = g - 0.2;
            //     b = b - 0.2;
            // }
            // let R = r;
            // let G = Math.floor(g * 255);
            // let B = Math.floor(g * 255);

           // let alphA = 0.8;
            for (let i = 0; i< buffer.length; i++) {
                for (let j = 0; j < buffer[i].length; j++) {
                    let v = buffer[i][j]* 0.5 + 0.5;
                    canvasCtx.fillRect(i*WIDTH/buffer.length
                                        , j * HEIGHT/buffer[i].length
                                        , (i+1) * WIDTH/buffer.length
                                        , (j+1) * HEIGHT/buffer[i].length);
                    }
            }};
        draw();
    })
    .catch((err) => {console.log(err);});



function hzToMel(f) {
    return 1127 * Math.log(1 + f/700)
}

function melToHz(f) {
    return 700 * (Math.exp(f / 1127)-1)
}

const DCTsize = 11;
function DCT(input) {
    let N = input.length;
    let output = new Float32Array(input.length);

    for (let i = 2; i < 2 + DCTsize; i++) {
        let k = i - 2;
        output[k] = 0;
        for (let n = 0; n < N; n++) {
            output[k] += input[n] * Math.cos(Math.PI/N * (n+0.5) * k);
        }
    }
    return output;
}

// -------------------------- code for rectangle window function --------------------------
function fromFFTRect(input) {
    const numBins = 26;
    const output = new Uint8Array(numBins);

    const melWidth = hzToMel(audioCtx.sampleRate / 2) / numBins;

    for (let i=0; i < output.length; i++){
        let minHz = melToHz(i * melWidth);
        let maxHz = melToHz((i + 1) * melWidth);

        let minInputIndex = Math.floor(minHz / fftBinWidth);
        let maxInputIndex = Math.floor(maxHz / fftBinWidth);

        for (let j = minInputIndex; j < maxInputIndex; j++) {
            output[i] += input[j];
        }
    }
    return output;
}
