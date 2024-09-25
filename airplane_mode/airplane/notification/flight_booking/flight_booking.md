*Flight Departure Reminder*

Your flight {{ doc.name }} is scheduled to depart soon.

*Details*

• Flight Number: {{ doc.airplane }}
• Departure Date: {{ doc.date_of_departure }}
• Departure Time: {{ doc.time_of_departure }}
• From: {{ doc.source }} ({{ doc.source_airport_code }})
• To: {{ doc.destination }} ({{ doc.destination_airport_code }})
• Duration: {{ doc.duration // 3600 }} hours

Please ensure that you arrive at the airport at least 2 hours before departure.

{% if comments %}
*Last Note:*
{{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}

Thank you for flying with {{doc.airplane}}!
