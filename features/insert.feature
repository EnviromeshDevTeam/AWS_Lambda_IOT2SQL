Feature: Amazon Lambda correctly inserts new data from Internet of Things (IoT) Service

    Scenario Outline: IoT Service rule is triggered. Passes a structured set of data to this Lambda. Lambda transforms and inserts data to database 

        Scenario: Data Transformation 

            Given Amazon IoT sends data
            When Lambda is automatically activated
            Then Data is correctly handled into a usable form for the database

        Scenario: Database Insert

            Given Amazon IoT sends data
            When Data is transformed
            Then Transformed Data is saved to Database
            But If Database save fails, Save is automatically prevented            

