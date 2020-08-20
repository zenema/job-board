self.addEventListener('install', function(e) {
    e.waitUntil(
      caches.open('vojobo-store').then(function(cache) {
        return cache.addAll([
          './src/index.html',
        //   '/pwa-examples/a2hs/index.js',
        //   './style.css',
        ]);
      })
    );
   });
   
   self.addEventListener('fetch', function(e) {
     console.log(e.request.url);
     e.respondWith(
       caches.match(e.request).then(function(response) {
         return response || fetch(e.request);
       })
     );
   });