var sumFourDivisors = function(nums) {
    let divSum = 0;

    for (let n of nums) {
        let divCount = 0, inSum = 0;

        for (let d = 1; d * d <= n; d++) {
            if (n % d === 0) {
                let other = n / d;

                if (d === other) {
                    divCount++;
                    inSum += d;
                } else {
                    divCount += 2;
                    inSum += d + other;
                }

                if (divCount > 4)
                    break;
            }
        }

        if (divCount === 4)
            divSum += inSum;
    }

    return divSum;
};