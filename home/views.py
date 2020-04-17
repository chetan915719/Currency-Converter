from django.shortcuts import render
from . import converter

# Create your views here.
def index(request):

    code = ['AFN', 'EUR', 'ALL', 'DZD', 'USD', 'EUR', 'AOA', 'XCD', 'XCD', 'ARS', 'AMD', 'AWG', 'AUD', 'EUR', 'AZN', 'BHD', 'BSD', 'BDT', 'BBD', 'BYN', 'EUR', 'BZD', 'XOF', 'BMD', 'INR', 'BTN', 'BOB', 'BOV', 'USD', 'BAM', 'BWP', 'NOK', 'BRL', 'USD', 'BND', 'BGN', 'XOF', 'BIF', 'CVE', 'KHR', 'XAF', 'CAD', 'KYD', 'XAF', 'XAF', 'CLP', 'CLF', 'CNY', 'AUD', 'AUD', 'COP', 'COU', 'KMF', 'CDF', 'XAF', 'NZD', 'CRC', 'XOF', 'HRK', 'CUP', 'CUC', 'ANG', 'EUR', 'CZK', 'DKK', 'DJF', 'XCD', 'DOP', 'USD', 'EGP', 'SVC', 'USD', 'XAF', 'ERN', 'EUR', 'ETB', 'EUR', 'FKP', 'DKK', 'FJD', 'EUR', 'EUR', 'EUR', 'XPF', 'EUR', 'XAF', 'GMD', 'GEL', 'EUR', 'GHS', 'GIP', 'EUR', 'DKK', 'XCD', 'EUR', 'USD', 'GTQ', 'GBP', 'GNF', 'XOF', 'GYD', 'HTG', 'USD', 'AUD', 'EUR', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'XDR', 'IRR', 'IQD', 'EUR', 'GBP', 'ILS', 'EUR', 'JMD', 'JPY', 'GBP', 'JOD', 'KZT', 'KES', 'AUD', 'KPW', 'KRW', 'KWD', 'KGS', 'LAK', 'EUR', 'LBP', 'LSL', 'ZAR', 'LRD', 'LYD', 'CHF', 'EUR', 'EUR', 'MOP', 'MKD', 'MGA', 'MWK', 'MYR', 'MVR', 'XOF', 'EUR', 'USD', 'EUR', 'MRO', 'MUR', 'EUR', 'XUA', 'MXN', 'MXV', 'USD', 'MDL', 'EUR', 'MNT', 'EUR', 'XCD', 'MAD', 'MZN', 'MMK', 'NAD', 'ZAR', 'AUD', 'NPR', 'EUR', 'XPF', 'NZD', 'NIO', 'XOF', 'NGN', 'NZD', 'AUD', 'USD', 'NOK', 'OMR', 'PKR', 'USD', 'PAB', 'USD', 'PGK', 'PYG', 'PEN', 'PHP', 'NZD', 'PLN', 'EUR', 'USD', 'QAR', 'EUR', 'RON', 'RUB', 'RWF', 'EUR', 'SHP', 'XCD', 'XCD', 'EUR', 'EUR', 'XCD', 'WST', 'EUR', 'STD', 'SAR', 'XOF', 'RSD', 'SCR', 'SLL', 'SGD', 'ANG', 'XSU', 'EUR', 'EUR', 'SBD', 'SOS', 'ZAR', 'SSP', 'EUR', 'LKR', 'SDG', 'SRD', 'NOK', 'SZL', 'SEK', 'CHF', 'CHE', 'CHW', 'SYP', 'TWD', 'TJS', 'TZS', 'THB', 'USD', 'XOF', 'NZD', 'TOP', 'TTD', 'TND', 'TRY', 'TMT', 'USD', 'AUD', 'UGX', 'UAH', 'AED', 'GBP', 'USD', 'USD', 'USN', 'UYU', 'UYI', 'UZS', 'VUV', 'VEF', 'VND', 'USD', 'USD', 'XPF', 'MAD', 'YER', 'ZMW', 'ZWL', 'XBA', 'XBB', 'XBC', 'XBD', 'XTS', 'XXX', 'XAU', 'XPD', 'XPT', 'XAG', 'AFA', 'FIM', 'ALK', 'ADP', 'ESP', 'FRF', 'AOK', 'AON', 'AOR', 'ARA', 'ARP', 'ARY', 'RUR', 'ATS', 'AYM', 'AZM', 'RUR', 'BYR', 'BYB', 'RUR', 'BEC', 'BEF', 'BEL', 'BOP', 'BAD', 'BRB', 'BRC', 'BRE', 'BRN', 'BRR', 'BGJ', 'BGK', 'BGL', 'BUK', 'HRD', 'HRK', 'CYP', 'CSJ', 'CSK', 'ECS', 'ECV', 'GQE', 'EEK', 'XEU', 'FIM', 'FRF', 'FRF', 'FRF', 'GEK', 'RUR', 'DDM', 'DEM', 'GHC', 'GHP', 'GRD', 'FRF', 'GNE', 'GNS', 'GWE', 'GWP', 'ITL', 'ISJ', 'IEP', 'ILP', 'ILR', 'ITL', 'RUR', 'RUR', 'LAJ', 'LVL', 'LVR', 'LSM', 'ZAL', 'LTL', 'LTT', 'LUC', 'LUF', 'LUL', 'MGF', 'MWK', 'MVQ', 'MLF', 'MTL', 'MTP', 'FRF', 'FRF', 'MXP', 'RUR', 'FRF', 'MZE', 'MZM', 'NLG', 'ANG', 'NIC', 'PEN', 'PEH', 'PEI', 'PES', 'PLZ', 'PTE', 'FRF', 'ROK', 'RON', 'ROL', 'RUR', 'FRF', 'FRF', 'FRF', 'ITL', 'CSD', 'EUR', 'SKK', 'SIT', 'ZAL', 'SDG', 'RHD', 'ESA', 'ESB', 'ESP', 'SDD', 'SDP', 'SRG', 'CHC', 'RUR', 'TJR', 'IDR', 'TPE', 'TRL', 'TRY', 'RUR', 'TMM', 'UGS', 'UGW', 'UAK', 'SUR', 'USS', 'UYN', 'UYP', 'RUR', 'VEB', 'VEF', 'VEF', 'VNC', 'YDD', 'YUD', 'YUM', 'YUN', 'ZRN', 'ZRZ', 'ZMK', 'ZWC', 'ZWD', 'ZWD', 'ZWN', 'ZWR', 'XFO', 'XRE', 'XFU'] 
    
    context = {
        'codes' : code,
    }

    access_key = 'f3f3b115fbc866af5825a4aef8ea8fb2'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=',access_key)

    if request.method == 'POST':
        form = request.POST
        c = converter.Currency_convertor(url)
        f_country = form['from_country']
        t_country = form['to_country']
        rate = c.convert(f_country,t_country)
        return render(request,"home/home.html",{'codes':code , 'rate':rate})
    
    return render(request,"home/home.html",context)


def about(request):
    context = {
        'title' : 'About',
    }
    return render(request,'home/about.html', context)