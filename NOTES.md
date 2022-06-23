## Extension
### Issues
- When testing generic cosmetic rules the source of the element is the current pages' URL so when said URL is part of an exeption rule an element which should be blocked by the generic rule is let through
	- We need a way to verify that the current site does not have an exeption rule attached to it, otherwise our test will deduce that no lists are installed because none of the elements were blocked
	- Maybe we can use a rule which is part of most browsers filter lists (Easylist would be the best candidate) to check wether it is blocked and when it isn't we deduce that the page has an exeption attached to it
		- However in doing so we omit all the configurations where Easylist is not installed and thus our rule would not be blocked on any site. Which leaves out a lot of odd configurations which are arguably more interesting to find for fingerprinting
	-> One possible solution is to ditch the pages where none of the tests were blocked when the same rules are blocked on other pages. This way our testing is not hindered by exeption rules or trusted sites on which the adBlocker is disabled
- Typical network rules seem to work as expected so far

## Plan
Global data on which tests pass (json) `GlobalTestData`
Algorithm to find which lists are installed based on `GlobalTestData` => ***AmIUnique* code**

Global database of `BustURLs`

### Network rules
Should not have much issue

### Cosmetic rules
Local data on tests which pass on each page `PageTestData`

> If none of the tests pass => test run is ignored and the page URL is added to `BustURLs`

> Otherwise `GlobalTestData` is updated with the results