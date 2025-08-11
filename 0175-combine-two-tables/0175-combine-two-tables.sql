select FirstName, LastName, City, State
from person
left join address
using (PersonId)