// xapi-slide.js
let tincan;
const actor = {
  name: "Mokynis",
  mbox: "mailto:mokynis@example.com"
};

let slideStartTime;

window.addEventListener("load", function () {
  tincan = new TinCan({
    recordStores: [
      {
        endpoint: "https://xapi-quiz.lrs.io/xapi/",
        username: "9f334b30-c044-4cea-b67f-ea772ca62a76",
        password: "596bd54a-ad72-4751-9699-81b3eeb617f2",
        allowFail: false
      }
    ],
    actor: actor
  });
  console.log("TinCan initialized:", tincan);

  slideStartTime = new Date();
});

function sendSlideExperienceAndNext(targetUrl) {
  const slideId = window.location.href;
  const now = new Date();
  const durationSeconds = ((now - slideStartTime) / 1000).toFixed(2);
  const platform = navigator.userAgent;

  const experiencedStatement = {
    verb: {
      id: "http://adlnet.gov/expapi/verbs/experienced",
      display: { "en-US": "experienced" }
    },
    object: {
      id: slideId,
      definition: {
        name: { "en-US": document.title },
        description: { "en-US": "Slide content viewed before questions." }
      },
      objectType: "Activity",
    },
    result: {
      duration: `PT${durationSeconds}S`
    },
    context: {
      platform: platform,
      contextActivities: {
        parent: [{
          id: "http://example.com/course/golf-intro",
          definition: {
            name: { "en-US": "Golf Course" },
            description: { "en-US": "General introduction to golf basics." }
          },
          objectType: "Activity"
        }]
      }
    },
    timestamp: now.toISOString()
  };

  try {
    tincan.sendStatement(experiencedStatement, function (err, xhr) {
      console.log("Navigation fired after xAPI send.");
      window.location.href = targetUrl;
    });
  } catch (e) {
    console.error("Failed to send experienced statement:", e);
    window.location.href = targetUrl;
  }
}
