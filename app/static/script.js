function iniciarMap(){
    var coord = {lat:-33.51106247301101,lng: -70.75253511849834};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}