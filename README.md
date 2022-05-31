# TechChallengeExercices
This project contains solutions to 2 technical challenge exercices

- Challenge 1:

    - Suppose we want to show a map to visualize the annual net generation of power plants of the US. The challenge consists of the following requirements:

        - We want to display the top N plants in terms of annual net generation.

        - On the map we want to show absolute value and percentage of the annual net generation by federal state.

        - We want to be able to filter by state so we can zoom in.

        - The data usually comes as excel file -  https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid (eGRID2016 Data File)

        - Built JUST a python backend that backs this map with a REST API.

        - Bonus: deployment of the solution in a cloud service.

 

- Challenge 2:

    - Attached is a csv file which contains image data referenced by the column depth. The rest of columns (200) represent image pixel values from 0 to 255 at each depth. The challenge consists on the following requirements:

        - The image size is relatively big. Hence, there is a need to resize the image width to 150 instead of 200.

        - The resized image has to be stored in a database.

        - An API is required to request image frames based on depth_min and depth_max.  

        - Apply a custom color map to the generated frames.

        - The solution should be based on Python.

        - Bonus: deployment of the solution in a cloud service.

- Solution:

    - To get image frames with minimum depth (between 9000.1 and 9546.0) The image is already resized and is in the database:
        - parameters: "min_depth" "max_depth" (they must both be present)
        https://techchall123.herokuapp.com/image-frames?min_depth=9000.1&max_depth=9200.0

    - The function is returning a binary so to read it paste it in this website:
        https://onlinepngtools.com/convert-base64-to-png


    - To get the top N plants in terms of annual net generation (use "number" parameter):
        https://techchall123.herokuapp.com/top-plants?number=10



    - To get absolute value and percentage of the annual net generation by federal state.
        https://techchall123.herokuapp.com/net-by-state


    - To filter Data by state so we can zoom in (parameter "state"):
        https://techchall123.herokuapp.com/filter-by-state?state=AZ
