Route::post('/withdraw', function (Request $request) use ($dbFile) {
    $accountNumber = $request->input('account_number');
    $amount = (float) $request->input('amount');

    $db = getDbData($dbFile);
    $accIdx = array_search($accountNumber, array_column($db['accounts'], 'account_number'));

    if ($accIdx === false) {
        return response()->json(['error' => 'La cuenta no existe'], 400);
    }

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
});