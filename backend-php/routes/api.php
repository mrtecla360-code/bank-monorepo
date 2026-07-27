develop
Route::get('/balance/{account_number}', function ($account_number) use ($dbFile) {
    $db = getDbData($dbFile);
    $accIdx = array_search($account_number, array_column($db['accounts'], 'account_number'));

Route::post('/withdraw', function (Request $request) use ($dbFile) {
    $accountNumber = $request->input('account_number');
    $amount = (float) $request->input('amount');

    $db = getDbData($dbFile);
    $accIdx = array_search($accountNumber, array_column($db['accounts'], 'account_number'));
main

    if ($accIdx === false) {
        return response()->json(['error' => 'La cuenta no existe'], 400);
    }

 develop
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

    if ($db['accounts'][$accIdx]['balance'] < $amount) {
        return response()->json(['error' => 'Fondos insuficientes para el retiro'], 400);
    }

    $db['accounts'][$accIdx]['balance'] -= $amount;
    $db['transactions'][] = [
        'type' => 'WITHDRAWAL',
        'account' => $accountNumber,
        'amount' => $amount
    ];

    saveDbData($dbFile, $db);

    return response()->json([
        'status' => 'success',
        'message' => 'Retiro exitoso',
        'nuevo_saldo' => $db['accounts'][$accIdx]['balance']
    ]);
main
});