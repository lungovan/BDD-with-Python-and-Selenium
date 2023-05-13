Feature: Upload Page

  Background: Open Upload page
    Given I have navigated to the Upload page

  Scenario: Verify Upload page contents are correct
    Then The page title is "File Upload Demo"
    And The page contains a file input
    And The page contains text "Select file to send(max 196.45 MB)"
    And The page contains a checkbox that is unchecked
    And The page contains a term text "I accept terms of service"
    And The page contains a button "Submit File"

  Scenario: Verify user can upload a valid file successfully
    When User select a valid file to upload
    Then The upload spinner displays
    Then The page display the upload successful message: "1 file(newline)has been successfully uploaded."

#  Scenario: Verify error message display when user select invalid file
#    When User select an invalid file to upload that exceed the max size
#    Then The page display the error message: "File exceed the limit size"