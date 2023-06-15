
# Affinity Answers Assignment

## 1. BestDelivery Courier Company Issue

#### Problem Statement
BestDelivery Courier Company has an issue. Many parcels they get to deliver have the wrong PIN code and that leads to packages going to the wrong location and then someone figuring out manually that the PIN code is wrong from the other parts of the address. You are the programmer who has to fix this issue by writing a program that takes as input a free flowing address and checking if the PIN code indeed corresponds to the address mentioned. Use this free API postalpincode.in/Api-Details for the purpose of PIN code identification.

#### Solution

The BestDeliveryCourier Python File contains the code to check for the valid addresses using the pincode.

A. get_correct_pincode(address) method:

        Input - address, the address to which the pincode is to be verified for.

        Output - pincode form the address

B. check_for_correct_address(address, pincode) method:

        Input - address, pincode, the pincode is used to fetch the postoffices from the api https://api.postalpincode.in/pincode/560050

        Output - True if the pincode is found to be correct for the given address, False if it is incorrect

#### Running the File

###### Step 1: install the requests module
        pip install requests

###### Step 2 : run the file using python
        python BestDeliveryCourier.py

## 2. Rfam Data

#### Problem Statement

A. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)

Answer: 

- 8 Different types of tigers can be found in the taxonomy table of the dataset

        SELECT count(distinct(species)) FROM Rfam.taxonomy WHERE species LIKE '%Panthera tigris%';

- ncbi_id = 9695

        SELECT ncbi_id,species FROM Rfam.taxonomy WHERE species LIKE '%Panthera tigris sumatrae%';

B. Find all the columns that can be used to connect the tables in the given database.

Answer:

- Main Tables:

        1. family
        2. rfamseq
        3. full_region
        4. clan
        5. clan_membership
        6. taxonomy

- Columns that can be used:

        1. family (rfam_acc) > clan_membership (rfam_acc)(clan_acc) > clan (clan_acc)
        2. family (rfam_acc) > clan_membership (rfam_acc)(clan_acc) > full_region (rfam_acc)
        3. rfamseq (ncbi_id) > taxonomy (ncbi_id)
        4. family (rfam_acc) > full_region (rfam_acc)

c. Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)

Answer:

- Count of all types of Rice (Scientific Name: Oryza)
        
    Result: 42

        SELECT count(*) FROM Rfam.taxonomy WHERE species LIKE 'Oryza%';

- Type of Rice with longest DNA Sequence:

    Result: 39946 | Oryza sativa Indica Group | 47244934

        SELECT taxonomy.ncbi_id, taxonomy.species, rfamseq.length 
        FROM taxonomy 
        LEFT JOIN rfamseq
        ON taxonomy.ncbi_id = rfamseq.ncbi_id
        WHERE taxonomy.species LIKE 'Oryza%' 
        ORDER BY rfamseq.length DESC
        LIMIT 1;

d. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

Answer:

- Result: Stored in csv file named "page9_rows15.csv"

        select rf.ncbi_id, rf.accession, max_length, taxonomy.species
        from
        (select ncbi_id, accession, max(length) as max_length from rfamseq 
        where length>1000000
        group by ncbi_id) as rf
        inner join taxonomy on taxonomy.ncbi_id = rf.ncbi_id
        order by max_length desc
        limit 15 offset 120;

## 3. Bash File - Unix Commands

#### Problem Statement

You are given this URL amfiindia.com/spages/NAVAll.txt Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a tsv file.

#### Solution

- The URL of the input file to be downloaded was set as the value of the input_url variable.
- The variable output_file was set to the desired path of the TSV output file.
- The input file was downloaded from the specified URL using the curl command and saved as the output_file.
- Then, awk was used to extract the fourth and fifth fields from each line, presuming that the fields were separated by semicolons (;). The print statement separated the extracted fields with tabs (t). The output was saved in the output_file.tmp temporary file.
- grep was utilised to eliminate lines that matched the header line ("Scheme NametAsset Value") and lines with empty fields. The output was then written back to the output_file after being filtered.
- The temporary file (output_file.tmp) was finally deleted.
- The extracted Scheme Name and Asset Value fields were saved in the output.tsv file


#### Problem Statement

And ever wondered if this data should not be stored in JSON?

Solution:

- The size of data may be a reason for not storing data in the josn File.
- There is no fixed maximum size for a JSON file specified in the JSON format but Memory and Performance may be one of the reasons to not store in a json file.
