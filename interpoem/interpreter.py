import json

def interpret_poem(poem):
    html_content = f"<html><head><title>{poem['title']}</title><style>.line {{ cursor: pointer; }}</style></head><body>"
    html_content += f"<h1>{poem['title']}</h1><h2>by {poem['author']}</h2><div id='poem'>"

    for stanza in poem['stanzas']:
        html_content += "<div class='stanza'>"
        for line in stanza:
            html_content += f"<div class='line' data-events='{json.dumps(line['events'])}'>{line['text']}</div>"
        html_content += "</div>"

    html_content += "</div><script>"
    html_content += """
    document.querySelectorAll('.line').forEach(line => {
        const events = JSON.parse(line.dataset.events);
        if (events) {
            Object.keys(events).forEach(eventType => {
                line.addEventListener(eventType, () => {
                    events[eventType].forEach(action => {
                        if (action.change_text) {
                            line.textContent = action.change_text;
                        } else if (action.play_audio) {
                            new Audio(action.play_audio).play();
                        } else if (action.display_image) {
                            const img = document.createElement('img');
                            img.src = action.display_image;
                            line.appendChild(img);
                        } else if (action.set_variable) {
                            // Add logic to set variables
                        }
                    });
                });
            });
        }
    });
    """
    html_content += "</script></body></html>"
    return html_content
