from unidecode import unidecode


def convert_row(row: list):
    """
    Takes in a row and returns row in XML format.

            Parameters:
                row (list): row

            Returns:
                xml_template (str): xml-formatted string
    """

    level, course_name, course_num, course_ttl, credits = ["", "", "", "", 0]

    course_name = row[11]
    course_num = row[12]
    course_ttl = unidecode(
        row[13] if "&" not in row[13] else row[13].replace("&", "&amp;")
    )

    # CHECK IF LEVEL DATA COMES IN AS AN INT OR STR
    if isinstance(row[12], int):
        level = row[12]
    elif isinstance(row[12], str):
        if len(row[12]) == 3:
            level = int(row[12])
        else:
            level = int(row[12][:2])

    # FORMAT LEVEL DATA
    if level >= 500:
        level = "GRADUATE"
    else:
        level = "UNDERGRADUATE"
    #     level = "CERTIFICATE" -- don't include

    if isinstance(row[14], int):
        credits = abs(float(row[14]))
    elif isinstance(row[14], str):
        if len(row[14]) <= 2:
            credits = abs(float(row[14]))
        else:
            credits = abs(float(row[14][1]))

    xml_template = """\n\t\t<AF_Course>
            <Crs_Subject>%s</Crs_Subject>
            <Crs_Number>%s</Crs_Number>
            <Crs_Title>%s</Crs_Title>
            <Crs_LongTitle>%s</Crs_LongTitle>
            <Crs_Credits>%s</Crs_Credits>
            <Crs_Level>%s</Crs_Level>
            <Prerequisites>NONE</Prerequisites>
            <Crs_Description>NONE</Crs_Description>
            <Crs_Materials>NONE</Crs_Materials>
        </AF_Course>"""

    # formats course credits: since it either comes in negative or as a tuple
    return (
        xml_template
        % (
            course_name,
            course_num,
            course_ttl,
            course_ttl,
            credits,
            level,
        )
        if credits > 0
        else ""
    )
    # subj, num, title, ltitle, credits, level, pre_req, descr


def export_xml(data: list):
    """
    Takes in a matrix of data and exports it as an XML file

        Parameters:
            data (list): list to be converted
    """

    xml_header = """<?xml version="1.0" standalone="yes"?>
    <AF_Catalog>"""

    xml_footer = """
    </AF_Catalog>"""

    # code block only useful for local file run
    """
    with open("./xml_export.xml", "w") as file:
        file.write(xml_header)

        for row in data:
            file.write(convert_row(row))

        file.write(xml_footer)
    """

    file_data = xml_header

    for row in data:
        file_data += convert_row(row)

    file_data += xml_footer

    return file_data


def export_xml_with_x_rows(data: list, row_count: int = 1):
    """
    Takes in a matrix of data and exports it as an XML file, but only with x amount of rows

        Parameters:
            data (list): list to be converted
            rows (int): row count limit
    """

    xml_header = """<?xml version="1.0" standalone="yes"?>
    <AF_Catalog>"""

    xml_footer = """
    </AF_Catalog>"""

    # code block only useful for local file run
    """
    with open("./xml_export.xml", "w") as file:
        file.write(xml_header)

        counter = 0
        while counter < rows:
            file.write(convert_row(data[counter]))
            counter += 1

        file.write(xml_footer)

        file_data = xml_header
    """

    file_data = xml_header
    counter = 0

    while counter < row_count:
        file_data += convert_row(data[counter])
        counter += 1

    file_data += xml_footer

    return file_data
