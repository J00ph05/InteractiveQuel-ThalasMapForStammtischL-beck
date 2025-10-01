import json

# Bildgröße deiner Karte (Pixel)
w, h = 4096, 3072

# Orte laden
with open("orte.json", "r", encoding="utf-8") as f:
    orte = json.load(f)

# HTML Grundgerüst
html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Quel'Thalas</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    body, html {{ margin: 0; height: 100%; }}
    #map {{ width: 100%; height: 100%; }}
  </style>
</head>
<body>
  <div id="map"></div>

  <script>
    var map = L.map('map', {{
      crs: L.CRS.Simple,
      minZoom: -1,
      maxZoom: 4
    }});

    var w = {w}, h = {h};
    var imageBounds = [[0,0], [h,w]];
    L.imageOverlay('Quel-Thalas.jpg', imageBounds).addTo(map);
    map.fitBounds(imageBounds);
"""

# Marker aus JSON hinzufügen
for ort in orte:
    name = ort["name"]
    x, y = ort["coords"]
    link = ort["link"]
    html += f"""
    L.marker([{h-y}, {x}]).addTo(map)
      .bindPopup('<b>{name}</b><br><a href="{link}" target="_blank">Zur Wiki-Seite</a>');
    """

# HTML Ende
html += """
  </script>
</body>
</html>
"""

# Datei speichern
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ index.html wurde erfolgreich generiert!")