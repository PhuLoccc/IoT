// function initMap() {
//     new google.maps.Map(document.getElementById("map"), {
//       mapId: "7bb341dd6f6bb06",
//       center: { lat: 10.762622, lng: 106.660172 },
//       zoom: 150,
//     });
//   }
// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow

function initMap() {
  var location = httpGet("/location");
  var obj = JSON.parse(location)
  map = new google.maps.Map(document.getElementById("map"), {
    mapId: "7bb341dd6f6bb06",
    center: { lat: Number(obj.Latitude),lng: Number(obj.Longtitude)},
    zoom: 10,
  });
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
  
///lat: Number(httpGet("/Latitude")) , lng: Number(httpGet("/Longtitude"))