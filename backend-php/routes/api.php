Route::get('/balance/{account_number}', function ($account_number) use ($dbFile) {
    $db = getDbData($dbFile);
    $accIdx = array_search($account_number, array_column($db['accounts'], 'account_number'));

    if ($accIdx === false) {
        return response()->json(['error' => 'La cuenta no existe'], 400);
    }

    $acc = $db['accounts'][$accIdx];

    return response()->json([
        'status' => 'success',
        'account_number' => $acc['account_number'],
        'holder' => $acc['holder'],
        'balance' => $acc['balance']
    ]);
});
Route::get('/accounts', function () use ($dbFile) {
    $db = getDbData($dbFile);
    return response()->json(['status' => 'success', 'accounts' => $db['accounts']]);
});