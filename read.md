Fetch Webpage: Downloads BBC News homepage HTML
Parse HTML: Creates a searchable structure from the HTML
Find Headlines:
Looks for <div> elements with data-component="text-block" (BBC's headline containers)
Extracts text from <h3> tags inside these containers
Get Top 10: Takes first 10 headlines found
Display Results:
Prints headlines to console with numbering
Saves same headlines to headlines.txt
