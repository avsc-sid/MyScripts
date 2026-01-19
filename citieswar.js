const COORDS = [
    ['uranium', { lat: 51.40563008003729, lng: 30.057047392356946 }, 8],
    ['oil', { lat: 29.762586489236817, lng: -95.40819668113559 }, 8],
    ['steel', { lat: 67.85605887684014, lng: 19.808222511470678 }, 10],
    ['rare', { lat: 41.85017326997629, lng: 110.01484866676812 }, 8],
    ['food', { lat: 23.166700000000017, lng: 89.19999999999999 }, 8],
];
const sel = () => {
    let t, id;
    t = document.evaluate(
        "//span[contains(text(), 'To navigate, press the arrow keys.')]",
        document
    );
    id = t.iterateNext().id;
    t = document.evaluate(`//div[@aria-describedby='${id}']/img`, document);
    return t.iterateNext();
};

function center() {
    map.setCenter({ lat: 0, lng: 0 });
    map.setZoom(3);
}

google.maps.event.addListenerOnce(map, 'idle', function () {
    for (i = 0; i < COORDS.length; i++) {
        const coords = COORDS[i];

        setTimeout(() => {
            center();

            document.getElementById(coords[0]).click();
            console.log('select resource ' + coords[0]);

            map.setCenter(coords[1]);
            console.log('set center');

            setTimeout(() => {
                map.setZoom(19);
                console.log('set zoom');
            }, 1500);

            setTimeout(() => {
                const elem = sel();
                elem.click();
                if (elem) {
                    console.log('start generation');
                    const well = document.getElementById('createWell');
                    for (j = 1; j < coords[3]; j++) {
                        setTimeout(() => {
                            well.click();
                            console.log('gen ' + j);
                        }, 50 * j);
                    }
                }
            }, 4000);
        }, 10000 * i);
    }
    center();
});
