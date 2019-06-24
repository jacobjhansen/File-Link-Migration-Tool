# ****************************************************************************
# 
# FILE LINK MIGRATION TOOL
#
# 2019 JACOB HANSEN
# ______________________________
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# PURPOSE
# ______________________________
# 
# The Purpose of this tool is to determine the relationship between files located in separate locations,
# and provide a CSV file linking the files and their relative links within both locations. 
#
# INPUT
# ______________________________
# The input of this program must be two .CSV files formatted as follows:
# File 1: OldLocationFiles.csv

import csv

# Create Global Variables
OldLocationCounter = 0
SharePointCounter = 0
OldLocationFiles = set()
OldToNew = []
ErrorNum = 0

# Write all Old Location Files to set 'OldLocationFiles'
with open('OldLocationFiles.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        allData = ((row[1]).split('\\'))
        address = (allData[-2:])
        fileSize = row[2]

        oldPath = ''
        for item in allData:
            oldPath += item + '\\'
        oldPath  = oldPath[:-1]

        line = oldPath + ', '
        
        # Try to find file name and parent folder (To catch error if file is in root folder)
        try:
            line += address[-2] + '\\' + address[-1]
        except:
            ErrorNum += 1
            break

        line += ', '
        line += fileSize
        OldLocationFiles.add(line)

for item in OldLocationFiles:
    print(item)
print('Total Files Skipped due to Errors: ' + str(ErrorNum))

with open('NewLocationFiles.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        allData = ((row[1]).split('\\'))
        address = (allData[:-1])
        line = ''
        for item in address:
            line += item+'\\'