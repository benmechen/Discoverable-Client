//
//  ViewController.swift
//  Discoverable Client
//
//  Created by Ben Mechen on 19/07/2020.
//  Copyright © 2020 Ben Mechen. All rights reserved.
//

import UIKit
import Discoverable

class ViewController: UIViewController {

    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var sendButton: UIButton!
    @IBOutlet weak var connectButton: UIButton!
    
    var connectionService = Discoverable()
    var isConnected = false
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        connectionService.delegate = self
        
        // Do any additional setup after loading the view.
        sendButton.layer.cornerRadius = 12.5
        connectButton.layer.cornerRadius = 12.5
    }

    @IBAction func toggleConnection(_ sender: Any) {
        if (!isConnected) {
            connectionService.discover(type: "_discoverable._udp", on: 1024)
        } else {
            connectionService.close()
        }
    }
    
    @IBAction func send(_ sender: Any) {
        guard (textField.text != nil) else {
            return
        }
        
        connectionService.send(textField.text!)
    }
}

extension ViewController: DiscoverableDelegate {
    func connectionState(state: Discoverable.State) {
        DispatchQueue.main.async {
            switch state {
            case .connected:
                self.isConnected = true
                self.connectButton.setTitle("Disconnect", for: .normal)
                self.sendButton.isEnabled = true
            default:
                self.isConnected = false
                self.connectButton.setTitle("Connect", for: .normal)
                self.sendButton.isEnabled = false
            }
        }
    }
    
    func connectionStrength(strength: Float) {
        
    }
}
