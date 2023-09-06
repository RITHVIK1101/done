from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample HTML code you provided
html = '''
<div class="fluid-engine fe-64ed03ac50c0dd51a0b103dd">
    <div class="fe-block fe-block-yui_3_17_2_1_1693254535853_2978">
                                        <div class="sqs-block code-block sqs-block-code" data-block-type="23" id="block-yui_3_17_2_1_1693254535853_2978">
                                            <div class="sqs-block-content">
    
    
    <li class="list-item" style="" data-is-card-enabled="false">
                                                        <div class="list-item-media" style="margin-bottom: 4%; width: 100%;">
                                                            <div class="list-item-media-inner" data-aspect-ratio="3:4" data-animation-role="image">
                                                                <img class="list-image" data-load="false" data-mode="cover" data-use-advanced-positioning="true" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.7" src="https://app.evanscreekmedia.com/rest/image/player/2023-Angiuli.jpg?uuid=1b7c6aec-19fb-4721-ae00-f90cebde9b0b" data-loaded="true">
                                                            </div>
                                                        </div>
                                                        <div class="list-item-content">
                                                            <div class="list-item-content__text-wrapper">
                                                                <h2 class="list-item-content__title" style="max-width: 75%;">1 - Marcus Angiuli</h2>
                                                                <div class="list-item-content__description" style="margin-top: 1%; max-width: 75%;">
                                                                    <p class="" style="white-space:pre-wrap;">Sr  |  WR/FS  |  6'3"  |  202lbs</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>

    <li class="list-item" style="" data-is-card-enabled="false">
                                                        <div class="list-item-media" style="margin-bottom: 4%; width: 100%;">
                                                            <div class="list-item-media-inner" data-aspect-ratio="3:4" data-animation-role="image">
                                                                <img class="list-image" data-load="false" data-mode="cover" data-use-advanced-positioning="true" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.7" src="https://app.evanscreekmedia.com/rest/image/player/2023-Edmunds.jpg?uuid=1b7c6aec-19fb-4721-ae00-f90cebde9b0b" data-loaded="true">
                                                            </div>
                                                        </div>
                                                        <div class="list-item-content">
                                                            <div class="list-item-content__text-wrapper">
                                                                <h2 class="list-item-content__title" style="max-width: 75%;">2 - Jack Edmunds</h2>
                                                                <div class="list-item-content__description" style="margin-top: 1%; max-width: 75%;">
                                                                    <p class="" style="white-space:pre-wrap;">Sr  |  RB/LB  |  6'2"  |  220lbs</p>
                                                                </div>
                                                            </div>
                                                        </div>
    <li class="list-item" style="" data-is-card-enabled="false">
                                                        <div class="list-item-media" style="margin-bottom: 4%; width: 100%;">
                                                            <div class="list-item-media-inner" data-aspect-ratio="3:4" data-animation-role="image">
                                                                <img class="list-image" data-load="false" data-mode="cover" data-use-advanced-positioning="true" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.7" src="https://app.evanscreekmedia.com/rest/image/player/2023-Hodges.jpg?uuid=1b7c6aec-19fb-4721-ae00-f90cebde9b0b" data-loaded="true">
                                                            </div>
                                                        </div>
                                                        <div class="list-item-content">
                                                            <div class="list-item-content__text-wrapper">
                                                                <h2 class="list-item-content__title" style="max-width: 75%;">3 - Bryson Hodges</h2>
                                                                <div class="list-item-content__description" style="margin-top: 1%; max-width: 75%;">
                                                                    <p class="" style="white-space:pre-wrap;">Jr  |  WR/FS  |  6'2"  |  180lbs</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>
    <li class="list-item" style="" data-is-card-enabled="false">
                                                        <div class="list-item-media" style="margin-bottom: 4%; width: 100%;">
                                                            <div class="list-item-media-inner" data-aspect-ratio="3:4" data-animation-role="image">
                                                                <img class="list-image" data-load="false" data-mode="cover" data-use-advanced-positioning="true" style="width: 100%; height: 100%; object-position: 50% 50%; object-fit: cover;" data-parent-ratio="0.7" src="https://app.evanscreekmedia.com/rest/image/player/2023-Arens.jpg?uuid=1b7c6aec-19fb-4721-ae00-f90cebde9b0b" data-loaded="true">
                                                            </div>
                                                        </div>
                                                        <div class="list-item-content">
                                                            <div class="list-item-content__text-wrapper">
                                                                <h2 class="list-item-content__title" style="max-width: 75%;">4 - Jake Arens</h2>
                                                                <div class="list-item-content__description" style="margin-top: 1%; max-width: 75%;">
                                                                    <p class="" style="white-space:pre-wrap;">Jr  |  RB/LB  |  6'1"  |  215lbs</p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>                                                
    
</div>
'''

# Define the scraping code here
def scrape_player_information(html):
    soup = BeautifulSoup(html, 'html.parser')
    player_items = soup.find_all('li', class_='list-item')
    player_info_list = []

    for player_item in player_items:
        player_name = player_item.find('h2', class_='list-item-content__title').text.strip()
        player_details = player_item.find('div', class_='list-item-content__description').text.strip()
        details = player_details.split('|')
        position = details[1].strip()
        height = details[2].strip()
        weight = details[3].strip()
        player_info = {
            'name': player_name,
            'position': position,
            'height': height,
            'weight': weight
        }
        player_info_list.append(player_info)

    return player_info_list

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json()
    user_query = request_data['queryResult']['queryText']
    intent_display_name = request_data['queryResult']['intent']['displayName']

    if intent_display_name == 'Player Information':
        # Scrape player information
        player_info_list = scrape_player_information(html)

        if player_info_list:
            # Assuming user specifies a player number (e.g., "Player 1")
            player_number = user_query.lower().replace('player ', '').strip()
            for player_info in player_info_list:
                if player_number in player_info['name'].lower():
                    response_text = f"Here are the details for {player_info['name']}:\n" \
                                    f"Position: {player_info['position']}\n" \
                                    f"Height: {player_info['height']}\n" \
                                    f"Weight: {player_info['weight']}"
                    break
            else:
                response_text = f"Sorry, I couldn't find information for Player {player_number}."

        else:
            response_text = "I'm sorry, but there was an issue retrieving player information."

        response = {
            'fulfillmentText': response_text
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
