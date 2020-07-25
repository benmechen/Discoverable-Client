//
//  ViewController.swift
//  Discoverable Client
//
//  Created by Ben Mechen on 19/07/2020.
//  Copyright © 2020 Ben Mechen. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var sendButton: UIButton!
    @IBOutlet weak var connectButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        sendButton.layer.cornerRadius = 12.5
        connectButton.layer.cornerRadius = 12.5
    }


}
