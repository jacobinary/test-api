(function() {
  function getFormattedUserInfo() {
    var content = '';

    for (var prop in data.user.info) {
      var value = data.user.info[prop];
      if (typeof value !== 'string') {
        value = JSON.stringify(value);
      }

      content += prop.toUpperCase() + ': ' + value + '<br>';
    }

    return content;
  }

  function initMap(container) {
    google.charts.load('current', {
      packages: ['map'],
      mapsApiKey: data.map.apiKey
    });

    google.charts.setOnLoadCallback(function() {
      var loc = google.visualization.arrayToDataTable([
        ['Lat', 'Long', 'Description'],
        [data.user.info.position.latitude, data.user.info.position.longitude, getFormattedUserInfo()]
      ]);

      var map = new google.visualization.Map(container);

      map.draw(loc, {
        showTooltip: true,
        showInfoWindow: true,
        zoomLevel: 16
      });
    });
  }

  var mapContainer = document.getElementById('map');
  if (mapContainer && navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      data.user.info.position = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude
      };

      initMap(mapContainer);
    }, function() {
      mapContainer.innerHTML = 'Please ensure you\'re allowing the app to see your location';
    });
  }
})();