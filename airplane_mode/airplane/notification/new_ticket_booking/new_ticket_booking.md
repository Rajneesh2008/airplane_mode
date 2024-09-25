<p>Flight Departure Reminder</p>

<p>Your flight {{ doc.name }} is scheduled to depart soon.</p>

<p>Details</p>

<p>• Flight Number: {{ doc.airplane }}
• Departure Date: {{ doc.date_of_departure }}
• Departure Time: {{ doc.time_of_departure }}
• From: {{ doc.source }} ({{ doc.source_airport_code }})
• To: {{ doc.destination }} ({{ doc.destination_airport_code }})
• Duration: {{ doc.duration // 3600 }} hours</p>

<p>Please ensure that you arrive at the airport at least 2 hours before departure.</p>

<p>{% if comments %}
Last Note:
{{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}</p>

<p>Thank you for flying with {{doc.airplane}}!</p>
