```mermaid
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
graph LR;
user_created{{ fa:fa-arrow-right-arrow-left user_created &#8205}}:::topic --> streaming-user-created[fa:fa-rocket streaming-user-created &#8205];
streaming-user-created[fa:fa-rocket streaming-user-created &#8205] --> transform{{ fa:fa-arrow-right-arrow-left transform &#8205}}:::topic;


classDef default font-size:110%;
classDef topic font-size:80%;
classDef topic fill:#3E89B3;
classDef topic stroke:#3E89B3;
classDef topic color:white;
```