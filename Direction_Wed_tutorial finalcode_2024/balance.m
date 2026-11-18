

% Step 1: Read the text file
filename = 'all.csv';
dataTable = readtable(filename, 'Delimiter', ','); % Assuming tab-separated file


% Step 2: Define adjusted ranges
leftRange = 5:10:175;    % Left values in steps of 10
rightRange = 5:10:175;   % Right values in steps of 10
diffRange = -170:10:170; % Diff values in steps of 10
diffRange(diffRange == 0) = []; % Exclude Diff = 0
targetRows = 544;        % Target total number of rows

% Step 3: Initialize an empty table for the balanced data
balancedTable = table();

% Step 4: Get unique combinations of 'Target' and 'consistency'
uniqueGroups = unique(dataTable(:, {'Target', 'consistency'}), 'rows');

% Step 5: Process each group
for i = 1:height(uniqueGroups)
    % Extract the current group
    currentGroup = uniqueGroups(i, :);
    groupRows = ismember(dataTable(:, {'Target', 'consistency'}), currentGroup);
    groupData = dataTable(groupRows, :);
    
    % Create a grid of all possible (Left, Right) combinations
    [LeftGrid, RightGrid] = ndgrid(leftRange, rightRange);
    allCombinations = [LeftGrid(:), RightGrid(:)];
    
    % Calculate the Diff values for all combinations
    DiffValues = allCombinations(:, 1) - allCombinations(:, 2);
    
    % Filter combinations to include only those within the desired Diff range
    validIndices = ismember(DiffValues, diffRange);
    validCombinations = allCombinations(validIndices, :);
    validDiffValues = DiffValues(validIndices);
    
    % Create a table with valid combinations
    newRows = table();
    newRows.Left = validCombinations(:, 1);
    newRows.Right = validCombinations(:, 2);
    newRows.Diff = validDiffValues;
    
    % Add group-specific columns ('Target' and 'consistency')
    newRows.Target = repmat(currentGroup.Target, height(newRows), 1);
    newRows.consistency = repmat(currentGroup.consistency, height(newRows), 1);
    
    % Balance across Diff values
    diffCounts = histcounts(newRows.Diff, [diffRange - 5, diffRange(end) + 5]);
    minCountPerDiff = min(diffCounts(diffCounts > 0)); % Minimum non-zero count
    
    % Sample to balance Diff values
    balancedRows = table();
    for diffValue = diffRange
        rowsForDiff = newRows(newRows.Diff == diffValue, :);
        if ~isempty(rowsForDiff)
            % Sample rows to match the minimum count
            sampledRows = rowsForDiff(randperm(height(rowsForDiff), minCountPerDiff), :);
            balancedRows = [balancedRows; sampledRows]; %#ok<AGROW>
        end
    end
    
    % Append balanced rows for this group to the final table
    balancedTable = [balancedTable; balancedRows]; %#ok<AGROW>
end

% Step 6: Adjust the number of rows to match the target (600 rows)
if height(balancedTable) > targetRows
    % Randomly sample rows if we have too many
    balancedTable = balancedTable(randperm(height(balancedTable), targetRows), :);
elseif height(balancedTable) < targetRows
    % Oversample rows by repeating them to meet the target
    deficit = targetRows - height(balancedTable);
    % Use modulo indexing to cycle through rows if needed
    additionalRows = balancedTable(mod(1:deficit, height(balancedTable)) + 1, :);
    balancedTable = [balancedTable; additionalRows];
end

% Step 7: Save the balanced dataset as a CSV file
outputFilename = 'final_balanced_data_exclude_diff_0.csv'; % Name of the output CSV file
writetable(balancedTable, outputFilename);

% Display a message indicating successful save
disp(['Balanced data saved to: ' outputFilename]);
